#!/usr/bin/perl
use LWP::Simple;

my $text = get 'example.com';
open(FILENAME, '<', \$text);