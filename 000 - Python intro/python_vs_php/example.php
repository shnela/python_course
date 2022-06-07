<?php
// Single line comment
# Single line comment
/*Multi
line
comment
*/

$int_val = 1;
print("$int_val\n");

$float_val = 3.14;
print "$float_val\n";

$text1 = 'dog\'s bone';
$text2 = " and cat's one";
print($text1 . " " . $text2 . "\n");

for ($i = 0; $i <= 10; $i++) {
    print("$i " . $text1 . "\n");
}

$counter = 0;
while ($counter < 3) {
    print($counter . "\n");
    $counter++;
}

if ($counter == 0) {
    print('Not even started' . "\n");
} elseif ($counter == 3) {
    print('Everything is under control' . "\n");
} else {
    print("I'm confused.\n");
}

$animals = ['cow', 'sheep'];
print("$animals\n");
array_push($animals, 'dog');
print("$animals[0]\n");

$herd_count = [
    'cow' => 1,
    'sheep' => 5,
];
print($herd_count['sheep'] . "\n");
$herd_count['dog'] = 1;
$herd_count['sheep'] -= 1;
print($herd_count['dog'] . "\n");
print($herd_count['sheep'] . "\n");


function square($x) {
    return $x * $x;
}

print(square(3) . "\n");

class Dog {
  public $fierceness;

  function __construct($fierceness) {
    $this->fierceness = $fierceness;
  }
  function bark() {
    print(str_repeat("Woof! ", $this->fierceness) . "\n");
  }
}

(new Dog(2))->bark();


class ItalianDog extends Dog {
  function bark() {
    print(str_repeat("Bau! ", $this->fierceness) . "\n");
  }
}


(new ItalianDog(2))->bark();


function factorial($n) {
    if ($n == 0) {
        return 1;
    } else {
        return $n * factorial($n - 1);
    }
}


print(factorial(1) . "\n");
print(factorial(100) . "\n");
# print(factorial(10000) . "\n");

?>