#!/bin/bash
echo "Prime numbers from 1 to 100:"

for num in {2..100}
do
    is_prime=1

    for ((i=2; i<=num/2; i++))
    do
        if (( num % i == 0 )); then
            is_prime=0
            break
        fi
    done

    if (( is_prime == 1 )); then
        echo $num
    fi
done

