#!/usr/bin/perl
use LWP::Simple;

my $text = get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/test/test.cgi';
#open(FILENAME, '<', \$text);

print split(/./, $text);