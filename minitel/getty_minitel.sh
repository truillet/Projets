
#!/bin/sh

TTY=${1:-ttyAMA0}
BPS=1200

sudo stty -F "/dev/$TTY" $BPS istrip cs7 parenb -parodd brkint \
        ignpar icrnl ixon ixany opost onlcr cread hupcl isig icanon \
        echo echoe echok;

sudo agetty ttyAMA0 1200&
