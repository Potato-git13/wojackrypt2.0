linux-build:
	mkdir -p bin/linux-build/
	pyinstaller --onefile --distpath=bin/linux-build/ --name=wojackrypt2 main.py

clean:
	rm -rf build/ wojackrypt2.spec __pycache__/

clean-bin:
	rm -rf bin/

push-to-bin:
	sudo cp bin/linux-build/wojackrypt2 /usr/bin/

remove-from-bin:
	sudo rm /usr/bin/wojackrypt2
