testfolder="tests"


test1="RR-test1"
echo "-----------------"
echo "Performing $test1 tests..."
python simulator.py "$testfolder/input-$test1.txt" > /dev/null
cmp RR.txt "$testfolder/output-$test1-RR.txt" && echo "Test RR good" || echo "Test RR FAIL"
cmp SRTF.txt "$testfolder/output-$test1-SRTF.txt" && echo "Test SRTF good" || echo "Test SRTF FAIL"
echo "-----------------"
echo ""

test1="SRTF-test1"
echo "-----------------"
echo "Performing $test1 tests..."
python simulator.py "$testfolder/input-$test1.txt" > /dev/null
cmp RR.txt "$testfolder/output-$test1-RR.txt" && echo "Test RR good" || echo "Test RR FAIL"
cmp SRTF.txt "$testfolder/output-$test1-SRTF.txt" && echo "Test SRTF good" || echo "Test SRTF FAIL"
echo "-----------------"
echo ""

test1="SRTF-test2"
echo "-----------------"
echo "Performing $test1 tests..."
python simulator.py "$testfolder/input-$test1.txt" > /dev/null
cmp RR.txt "$testfolder/output-$test1-RR.txt" && echo "Test RR good" || echo "Test RR FAIL"
cmp SRTF.txt "$testfolder/output-$test1-SRTF.txt" && echo "Test SRTF good" || echo "Test SRTF FAIL"
echo "-----------------"
echo ""