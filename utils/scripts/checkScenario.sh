
echo " --------------------------------";
echo " Testing your SmartContract .... ";
echo " --------------------------------";
printf "
 Test Summary : 
"
echo " ------------------";
./utils/smartpy-cli/SmartPy.sh test ./contract/bettingGame.py ./test-build;
printf "
 Test Scenarios :
";
echo " -------------------"
cat ./test-build/Running the application_interpreted/scenario-interpreter-log.txt;
printf "

"
