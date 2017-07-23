#!/bin/env perl

use strict;
use warnings;

system("mkdir content") unless(-d 'content');
my $theme = './elegant';
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$year += 1900;
$mon = '0' . $mon if($mon<10);
$mday = '0' . $mday if($mday<10);
my $stamp = $year . $mon . $mday;
my $com = "git commit -m 'autofired$stamp'";
$com =~ s/autofired$stamp/$ARGV[0]/ if($ARGV[0]);
my @cmd = (
	"pelican -s pelicanconf.py -o ./ content",
	"git add --all ./",
 	$com,
	"git push -u origin master" 
);
$cmd[0] .= " -t $theme" if($theme);
foreach (@cmd){
	print "\n$_...\n";
	system("$_");
}
