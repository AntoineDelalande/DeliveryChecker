#!/bin/bash

echo "=== Test 0 : cas valide ==="
python3 deliverychecker.py '[[1,2],[3,4]]' '[1,2,3,4]'

echo
echo "=== Test 1 : cas valide ==="
python3 deliverychecker.py '[[1,3],[2,5]]' '[1,2,3,4,5]'

echo
echo "=== Test 2 : adresse manquante ==="
python3 deliverychecker.py '[[1,2],[5,6]]' '[1,2,3,4]'

echo
echo "=== Test 3 : dropoff avant pickup ==="
python3 deliverychecker.py '[[1,2]]' '[2,1]'

echo
echo "=== Test 4 : tous les pickups avant dropoffs ==="
python3 deliverychecker.py '[[1,4],[2,3]]' '[1,2,3,4]'

echo
echo "=== Test 5 : appel sans arguments ==="
python3 deliverychecker.py

echo
echo "=== Test 6 : appel 1 argument ==="
python3 deliverychecker.py '[[1,2]]'

echo
echo "=== Test 7 : appel 3 arguments ==="
python3 deliverychecker.py '[[1,2],[3,4]]' '[1,2,3,4]' 'extra_argument'


echo
echo "=== Test 8 : mauvais json ==="
python3 deliverychecker.py '[[1,]]' '[1,2]}'

echo
echo "=== Test 8 : monkey test ==="
python3 deliverychecker.py à aàç{§qsdkbf  sd"uze"