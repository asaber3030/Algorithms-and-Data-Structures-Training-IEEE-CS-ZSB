<?php
$n = 3;
$a = "BBW";
$s = 0;
$arr = [];
$j = 0;

for ($i = 0; $i < $n; $i++) {
  if ($a[$i] == "B") {
    $s++;
    $arr[$j] = $s;
    if ($i == $n - 1) {
      $j++;
    }
  } elseif ($s != 0) {
    $j++;
  }
}
print("First line: " . $j . '----');

for ($i = 0; $i < $j; $i++) {
  print("Second Line: " . $arr[$i]);
}
