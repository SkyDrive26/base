#!/usr/bin/perl
use LWP::Simple;

my $text = get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/test/test.txt';
#open(FILENAME, '<', \$text);

my ($main, $major, $minor) = split(/:/, $text);

print $main."\n";
print $major."\n";
print $minor."\n";