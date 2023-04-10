# 7.1. Найдите кнопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
http://suninjuly.github.io/xpath_examples

## CSS

1. div:last-of-type .btn:nth-of-type(3)
2. div:last-child .btn:nth-child(3)

## Xpath

1. (//div/button)[7]
2. //div[2]/button[3]
3. //div/button[text()='Gold']
4. //button[text()='Gold']
5. //button[contains(text(), 'Gold')]


# 7.2. Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
http://suninjuly.github.io/cats.html

## Xpath

1. //p[@class='card-text'] [text()='Fully charged cat'] или //p[@class='card-text' and text()='Fully charged cat']
2. //p[@class='card-text'] [contains(text(), 'Fully')] 
3. (//p[@class='card-text'])[3] 
4. //div[5]/div/div/p
5. //div[last()-1]/div/div/p