#  Place a bet for 0.5tz
# Betting rules : predict a number for bet and another number for seed (used to decide bet wiiner)
# when second user sends the number for bet, winner is decided and is awarded the money staked by both the first(0.5 tx) and second user(0.5 tz) i.e 1tz

import smartpy as sp

class BettingGame(sp.Contract):
    def __init__(self,initialOwner):
        # self.init(owner=initialOwner,idToBet = sp.map(tkey=sp.TNat,tvalue= sp.TList), bet=1, idToAccount=sp.map(tkey=sp.TNat,tvalue=sp.TAddress))
        self.init(owner=initialOwner,idToBet = sp.map(), bet=1)
        # List[0] = Number  List[1] = seed 
        
    @sp.entry_point
    def createBet(self,params):
        # params = { number, seed}
        sp.verify(sp.amount == sp.mutez(500000), message= 'Wrong amount sent')
        sp.verify(params.number > 0, message='Wrong Bet Number')
        sp.verify(params.number < 100, message='Wrong Bet Number')
        sp.set_type(params.number, sp.TNat)
        sp.set_type(params.seed, sp.TNat)
        self.data.idToBet[self.data.bet] = sp.record(number = params.number,seed = params.seed,creator=sp.sender)
        self.data.bet = self.data.bet + 1
        # return self.data.bet - 1;
        
    @sp.entry_point
    def realiseBet(self,params):
        # params = { bet, number, seed}
        sp.verify(sp.amount == sp.mutez(500000), message= 'Wrong amount sent')
        sp.verify(params.number > 0, message='Wrong bet number')
        sp.verify( params.number < 100,message='Wrong bet number')
        sp.verify(params.bet < self.data.bet, message='Invalid BET ID')
        sp.verify( params.bet > 0,message='Invalid BET ID')
        seed2 = params.seed % 100
        firstBetData = self.data.idToBet[params.bet]
        seed1 = firstBetData.seed % 100
        finalSeed = ( seed1 + seed2 ) % 100
        num1Diff = abs(finalSeed - firstBetData.number)
        num2Diff = abs(finalSeed - params.number)
        sp.if (num1Diff < num2Diff) :
            sp.send(firstBetData.creator,sp.tez(1))
        sp.else:
            sp.send(sp.sender,sp.tez(1))
            
            
    @sp.add_test(name = "Running the application")
    def test():
        scenario = sp.test_scenario()
        scenario.h1("Initialisation")
        deployer = sp.address("tz1PCVSQfsHmrKRgCdLhrN8Yanb5mwEL8rxu")
        player1 = sp.address("tz1U5E7U225tYk5uuNDpQpcQ2e4hCmekBadh")
        player2 = sp.address("tz1hHLY4AzGXrqzapnA3JYurGrPb5d3RnG7M")
        c1 = BettingGame(deployer)
        scenario += c1
        scenario.h2("Bet Creation")
        scenario += c1.createBet(number=43,seed=3452).run(sender=player1,valid=False)
        scenario += c1.createBet(number=101,seed=2314).run(sender=player1,amount=sp.mutez(500000),valid=False)
        scenario += c1.createBet(number=43,seed=3452).run(sender=player1,amount=sp.mutez(500000))
        scenario.h2("Bet Realisation")
        scenario += c1.realiseBet(bet=1,number=23,seed=5421).run(sender=player2,valid=False)
        scenario += c1.realiseBet(bet=1,number=123,seed=5421).run(sender=player2,amount=sp.mutez(500000),valid=False)
        scenario += c1.realiseBet(bet=1,number=23,seed=5421).run(sender=player2,amount=sp.mutez(500000))