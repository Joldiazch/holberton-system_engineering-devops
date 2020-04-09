#!/usr/bin/env bash
# display information for its subdomains www, lb-01, web-01 and web-02

print_msg()
{
	echo "$1 $2 $3" | awk '{text = "The subdomain " $2 " is a " $3 " record and points to "$1; print text}'
}

SUBS="www lb-01 web-01 web-02"
DOT="."
if [ "$2" ]
	then
		URL=$2$DOT$1
		IP="$(dig "$URL" +short)"
		RECORD="$(dig "$URL" | grep '^'"$URL" | cut -f4)"
		print_msg "$IP" "$2" "$RECORD"
else
	if [ "$1" ]
		then
			for sub in $SUBS; do
				URL=$sub$DOT$1
				IP="$(dig "$URL" +short)"
				RECORD="$(dig "$URL" | grep '^'"$URL" | cut -f4)"
				print_msg "$IP" "$sub" "$RECORD"
			done
	fi
fi
