<?PHP

$txtFile = fopen("../key.txt", "r") or die ("Unable to open file!");
$key = fread($txtFile,filesize("../key.txt"));
fclose($txtFile);

if($_GET['c'] != $key) {
    exit();
}

//Code goes here
