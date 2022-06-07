# Single line comment
=begin Multi
line
comment
=end

int_val = 1
puts(int_val)

float_val = 3.14
puts(float_val)

text1 = 'dog\'s bone'
text2 = " and cat's one"
puts(text1 + text2)

for i in 0..2
  puts(String(i) + ' ' + text1)
end

counter = 0
while counter < 3
    puts(counter)
    counter += 1
end

if counter == 0
    puts('Not even started')
elsif counter == 3
    puts('Everything is under control')
else
    puts("I'm confused.")
end

animals = %w(cow sheep)
puts(animals)
animals.push('dog')
puts(animals)

herd_count = {
    'cow' => 1,
    'sheep' => 5,
}
puts(herd_count)
herd_count['dog'] = 1
herd_count['sheep'] -= 1
puts(herd_count)


def square(x)
    x ** 2
end

puts(square(3))


class Dog
    def initialize(fierceness)
        @fierceness = fierceness
    end

    def bark()
        puts("Woof! " * @fierceness)
    end
end


Dog.new(2).bark()


class ItalianDog < Dog
    def bark()
        puts("Bau! " * @fierceness)
    end
end


ItalianDog.new(2).bark()


def factorial(n)
    n == 0 ? 1 : n * factorial(n - 1)
end


puts(factorial(1))
puts(factorial(100))
# puts(factorial(10000))