#!/bin/bash

#	USING RELEASE IN SIVIR:

#	$ ./release_sivir dev # -> 0.0.2
#	$ ./release_sivir compatible # -> 0.2.0
#	$ ./release_sivir imcompatible # -> 2.0.0

#getting the version
version=$(cat version)

#splitting dots
tokens=(${version//\./ })

#imcompatible version
imcomp=${tokens}

#compatible version
comp=${tokens[1]}

#development version
dev=${tokens[2]}

#increase development version
dev() {
	dev=$((dev+1))
}

#increase development version
compatible() {
	comp=$((comp+1))
	dev=0
}

#increase development version
imcompatible() {
	imcomp=$((imcomp+1))
	comp=0
	dev=0
}

#select wich version is and executes
case $1 in
	compatible) compatible ;;
	imcompatible) imcompatible ;;
	dev) dev ;;
	*) echo "Invalid" ;;
esac

#final version *.*.*
finalversion="$imcomp.$comp.$dev"

#checkout releases branch
git checkout releases

#push to releases branch
git push origin releases

#generates a release 
git tag -a "$finalversion" -m "Release $finalversion"

#push the release to github
git push --tags

echo $finalversion > version