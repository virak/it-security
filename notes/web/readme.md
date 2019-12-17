# LFI - Local File Inclusion

Being able to include a file from the site using certain part of the application.

## PHP filter

You can get the content of a php file using this filter:

> php://filter/read/=convert.base64-encode/resource=(yourfilename)