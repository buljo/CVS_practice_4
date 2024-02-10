<?php

function calculate_a($n) {
    if ($n == 1) {
        return 1;
    } else {
        if (($n % 2) != 0) {
          $n = $n - 1;
        }
        return calculate_a($n / 2) + 1;
    }
};
?>
