# Betting Game

## Objective: 

The objective of this project was to get familiar with tezos ecosystem. The game created in this project has leak points such as lack of random number which can enable the second user to always cheat and win the bet but that wasn't the goal. 
## Status :

- Completed the smart contract along with tests
- Smart Contract deployed to `carthagenet testnet` at `KT1G7sCguSaLjYFwFxKJEPFLNK3fWMpuvtrJ`
- Contract can be found on smartPy online ide [here](http://smartpy.io/dev/index.html?code=eJzNVm1v2zYQ_u5fcXAwVEJcwZJttOiiYXlbmi3NkjTdFhSBQYt0TESiNJKqaxf77zuKsizFcup2X2YggUTePXf33HOk9gCuYhIxIDBhGqaphL430svOHhwxrbl4AJnHTMEbyCSjPNJoKfJkwmRhbJyIoPiX6hmu1bYUYxScXOF_nQJlEaessJ9zLph0McR8xgTaRSkioKHxEVQBIj2J0UMngU7AVYlEi7D4SuZEmlfjlKSCLUBp8ogLkwVMMKliY8ql0g5WBvqzW3jWotr1pQvcY@Bj7Z0OT7JUalAJkTpbAFGgsk4niolSK17OSMIclXnHqdCSRNp90wH8UTaF8ZgLrsdjR7F42jPPnMS_z03R1sj89sDsembXSc1eWDfscXqbYiQIMbKXkMzRj2wR4vPtJdE9_YnEOSv2bi@40m7PsBT6PTB@h1GU5kKHz3ia10NKJVPKdaucvi2jVVC3VpNJ5mP_Ho0ubQPtim9WCkFUtsXDzwjFkL_FOEu50BWDkWREM4xmKcyIJIlqkGeXEPVLKZVegf_PupbM@8Qkny5Mk0hiCIHQ5p5rtnRGffPDGhLkgDwgmS_@lCnqvbRFKeoXbgucjeyVAv0J@muIEsGwZMvfAeAA_P7uEIrpsV5krAnSg7K9z9oaftosTdMp0cQrO_xxvYL9vbcNlzgvkjpl0iE04xetrRaLQEULUxkWiQhqBn4z4sTqqfG@D36tz5LpXIonJi_B_3E3IWESMVe7Kqk4af53cjIVi@1ygjY9fRtEiWCsDppU15I5F3h0cApHp7dwfvJsKgbIVLKDL5IcNJUDP5gKKovi6Mb@nWBGDa2s1LqOed@A9dG67twOLkj83orXKb32y6TcJ7bIn3_Cp1M0JRPlrF1fNsNYnt26X7DFr9G5BqF8Ck4V8KDCcGGt3GrKBXUaCZST18NNo0zfbSCzWLF2kGpS2zyrSdsYO0LpWDO8XgXeiFhk9yYXwnw4mIuXZFnMI6J5KrpuNZWFeW0IVcQEkTy1R43ZHa@WHHfDypv5TvfcXk1c1bEtfhani@KMssmZO87p6qV_dfzH@@upepvI324ejunFTF6@viNiMkrmpxev5ee8hpLFBDH8TZAPo9NXH4JgpO8eR3l@eZJdZ9F1wIaz44Q9HhE62wAJNkFmby_uhofLs7_k30uSicPBr3e5PJNXkxEd3IizV@9qIJFJov7NsSpwkxjYD9G8ha_A6ZoL5dgIo8lW09Vb37tWk@FwUJzt4WA4ClxP5sKxEglLgnrFXIe_EFTV7qh@37ewwcAftsLaUzPcOF6_K9xXi9gSrU16JZU3rE17TxKpXT7266zMJyjzGQ0DvyWfYKcqt4H7X0X_L9x@d0nbKP4X_zbcyg--). 

- FrontEnd not yet created (but i have used conseilJS in the past, so it shouldn't be difficult)

## Prerequisites :

- Python 3.x +
- Node v12.x +

## Setup & Run Steps :

1.  `npm install` it will install all your dependencies

## Its time to compile & Deploy

3.  `npm run sync` this is a syncing command. Whenever the compile_config is changed in config.json this command must be executed from the terminal. This command helps the bundle to reconfigure the compilation parameters according to the changes you have made.

4  `npm run compile` will build the contracts locally inside the folder ./contract_build.

5.  `npm run deploy` will deploy your contract with the params respect to your config.json

#### Configuring Deployment Parameters :

Inside the deploy_config section

- First is the Tezos node you want to use , It can be local or any remote node

* Next You can change the contract_code and contract_storage with the ones you want to deploy

- Set the parameters like amount, gas_limit, derivation_path etc

A Tezos **node** allows you deploy contract, make transaction etc.

Other Tezos Nodes :

- [https://tezos-dev.cryptonomic-infra.tech](https://tezos-dev.cryptonomic-infra.tech/)

* [https://carthagenet.SmartPy.io](https://carthagenet.smartpy.io/)

- [http://carthagenet.tezos.cryptium.ch:8732](http://carthagenet.tezos.cryptium.ch:8732/)

Conseil node is used to access conseil services and you need a API Key for that

- [https://conseil-dev.cryptonomic-infra.tech:443/](https://conseil-dev.cryptonomic-infra.tech/)

Use [https://nautilus.cloud](https://nautilus.cloud/) to access API KEY for Conseil node. Use [https://faucet.tzalpha.net/](https://faucet.tzalpha.net/) to obtain keys for any testing. You can use [http://smartpy.io/dev/faucetImporter.html](http://smartpy.io/dev/faucetImporter.html) to activate the keys obtained from faucet.

**Contract Specifications:**

- **contract_code** : It should refer to the Michelson Contract code you want to deploy.

- **contract_storage** : refers to the Michelson representation of the initial storage used for deployment

## Boilerplate Source 
[Bundle React by Tezsure](https://github.com/Tezsure/Bundle-react/)

## License

Licensed under the MIT. See the [LICENSE](https://github.com/Tezsure/Bundle-react/blob/master/LICENSE) file for details.
