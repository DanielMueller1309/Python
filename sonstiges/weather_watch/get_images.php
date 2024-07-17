<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$dir = 'radar_images';
if (!is_dir($dir)) {
    die(json_encode(['error' => 'Verzeichnis nicht gefunden: ' . $dir]));
}

$images = array_values(array_diff(scandir($dir), array('..', '.')));
if (empty($images)) {
    die(json_encode(['error' => 'Keine Bilder im Verzeichnis gefunden']));
}

$images = array_map(function($image) use ($dir) {
    return $dir . '/' . $image;
}, $images);

header('Content-Type: application/json');
echo json_encode([
    'status' => 'success',
    'images' => $images,
    'dir' => $dir,
    'scanned_images' => scandir($dir),
]);
?>
