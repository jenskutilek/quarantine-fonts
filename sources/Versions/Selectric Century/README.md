The Century type style from the IBM Selectric Composer

<img src="Selectric%20docs/century-8-title.jpg">

# Reviving the Selectric Century Fonts

Before you can start drawing a revival of a typeface originating from any mechanical system, you need to do the math.

## Unitized Glyph Widths

<img src="Selectric%20docs/CenturyMedium9.png" width="800" alt="">

<img src="Selectric%20docs/CenturyMedium8.png" width="800" alt="">

Images: 9pt and 8pt Century. Notice the identical set width of both font sizes.

The glyph widths of the IBM Composer are on a grid of 3 to 9 units per em. I figured the best grid setting for drawing an OpenType font would be 900 upm so that 1 composer unit corresponds to 100 font units.

Composer unit table (German):

| Units | Characters |
| ----: | -----------|
| 3     | i j l . , ‘ ’ - ; |
| 4     | I f r s t ( ) / : ! |
| 5     | J a c e g v z ä ü |
| 6     | P S b d h k n o p q u x y ö ß § * + = 0 1 2 3 4 5 6 7 8 9 |
| 7     | B C E F L T Z |
| 8     | A D G H K N O Q R U V X Y Ä Ö Ü w & % – ? |
| 9     | M W m |

The unit value assigned to each letter is the same for all Composer fonts.

One typographical point of the IBM system is 0.35277 mm in size; 1 pica = 12 points.

The composer units can be used at different nominal font sizes, allowing for a difference in font width, e.g. a condensed vs. extended letter width. The appropriate unit setting for a typeface/size combination is given as a color code.

| Color code | Units per pica | Width of 1 unit |
| ---------- | -------------: | --------------: |
| Red        | 12             | 0.3527 mm |
| Yellow     | 14             | 0.3024 mm |
| Blue       | 16             | 0.2645 mm |

For each font and size available, the color code and cap height are given:

| Font    | Size  | Color code | Cap height |
| ------- | ---:  | ---------- | ---------: |
| Century |  6 pt | blue       | 5.0 pt
| Century |  8 pt | yellow     | 6.0 pt
| Century |  9 pt | yellow     | 6.5 pt
| Century | 10 pt | red        | 7.0 pt
| Century | 11 pt | red        | 8.0 pt

As you can see, the 8/9 pt and 10/11 pt share the same unit setting, so their set width will actually be identical, but the letter height varies.

## Finding The Correct Scale

Drawing a font at 900 units per em is fine. It is close to the common 1000 upm that probably 99% of all OpenType CFF fonts use.

But to get the glyphs output at the correct size, we need to figure out if our scaling is correct. 

If tell our layout software to give us a 10 point font, the 900 font units are scaled to 10 points for display, so:

```
900 font units → 10 pt = 3.5277 mm
```

Dividing by 9, we get:

```
100 font units → 1.1111 pt = 0.3919666667 mm
```

Remember, 100 font units are 1 composer unit for our font-internal drawing purposes.

At the red setting, 1 composer unit equals 0.3527 mm, but the calculation shows our 100 font units correspond to 0.3919666667 mm. To get the correct output at 10 pt font size, we can set the units per em at export so as to make up for the difference.

We need to calculate a correction factor by dividing 0.3919666667 mm by 0.3527 mm and get 1.1113316323. To make the font smaller, the font units per em settings must be bigger, so we get 900 * 1.1113316323 = 1000 (incidentally, the standard upm setting).

Let's check if the math works out:

```
1000 font units → 10 pt = 3.5277 mm
```

Divide by 10, trivially:

```
100 font units → 1 pt = 0.3527 mm
```

Yay!

So for the different font sizes we get:

For 9 pt:

```
900 font units → 9 pt = 3.17493 mm  | ÷ 9
100 font units → 1 pt = 0.35277 mm
```

For the yellow setting, 1 composer unit should be 0.3024 mm, so we need to calculate the correction factor by dividing 0.35277 mm / 0.3024 mm = 1.1665674603. Our correct units per em setting is 900 * 1.1665674603 = 1050.

For 8 pt:

```
900 font units → 8 pt = 2.82216 mm        | ÷ 9
100 font units → 0.8889 pt = 0.313573 mm
```

As the 8 pt font also uses the yellow setting, 1 composer unit should again be 0.3024 mm, so we need to calculate the correction factor by dividing 0.313573 mm / 0.3024 mm = 1.0369477513. To make the font smaller, the font units per em settings must be bigger, so we get 900 * 1.0369477513 = 933.

For 11 pt:

```
900 font units → 11 pt = 3.88047 mm         | ÷ 9
100 font units → 1,222222 pt = 0.431163 mm
```

As the 11 pt font also uses the red setting like the 10 pt font, 1 composer unit should again be 0.3527 mm, so we need to calculate the correction factor by dividing 0.431163 mm / 0.3527 mm = 1.2224638503. To make the font smaller, the font units per em settings must be bigger, so we get 900 * 1.2224638503 = 1100.

## Cap Heights

As the Composer manual gives us the cap heights for each font and size, we can now calculate the cap heights in internal font units for each font size:

```
1100 / 11 * 8   = 800  (11 pt, 8 pt cap height)
1000 / 10 * 7   = 700  (10 pt, 7 pt cap height)
1050 /  9 * 6.5 = 758  (9 pt, 6.5 pt cap height)
 933 /  8 * 6   = 700  (8 pt, 6 pt cap height)
```

That should give us a hint as to how to scale our scans.

Scalable fonts, my ass! We need a different drawing for each font size.
