rc:
	pyrcc5 -o "audio_reactive_led_strip/resources/resources_rc.py" "audio_reactive_led_strip/resources/resources.qrc"

gui:
	pyuic5 --import-from="..resources" --output "audio_reactive_led_strip/gui/window.py" "audio_reactive_led_strip/gui/window.ui"

run:
	python cli.py

build:
	python setup.py build

clean:
	rm -rf build