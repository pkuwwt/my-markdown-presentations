
# Recipes for Linux Bash Commands

---

## How to use `case`

```bash
echo "Please talk to me ..."
while :
do
	read INPUT
	case $INPUT in
	    hello)
	    	echo "Hello yourself!"
	    	;;
	    bye)
	    	echo "See you again!"
			break
	    	;;
	    *)
	    	echo "I don't understand!"
	    	;;
	esac
done
```

---

## How to prompt from password

```bash
echo -n "Enter password>"
read -s password
echo
echo "$password"
```

---


