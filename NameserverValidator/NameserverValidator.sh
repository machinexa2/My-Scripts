#!/bin/bash
nmserver="/root/Wordlists/resolvers/resolver.txt"
nmvalidated="/root/Wordlists/resolvers/resolv.txt"
#rm $nmvalidated
dnsvalidator -tL $nmserver -threads 20 -o $nmvalidated
resolvconf="/root/Wordlists/resolvers/nameservers"


