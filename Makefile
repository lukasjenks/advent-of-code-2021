clean:
	find . -name '.idea' -exec rm -r {} \;
	find . -name '.vscode' -exec rm -r {} \;
	find . -name '*.iml' -exec rm -r {} \;
	find . -name '*.class' -exec rm -r {} \;
	find . -name 'out' -exec rm -r {} \;