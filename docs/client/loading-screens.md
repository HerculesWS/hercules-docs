Loading screens are graphics, that are shown when the client is loading map data, before entering the game or while
changing maps.

They are located inside the [GRF](./grf.md) in **data\texture\À¯ÀúÀÎÅÍÆäÀÌ½º** (data\texture\유저인터페이스), must
be of type JPEG and have to be called **loadingXX.jpg** where XX is a zero-based index (00, 01, 02...) and limited to
about 6-12 files depending on langtype (unless you have diffed *Unlimited Loading Screens* option).

You should prefer sizes of 4:3 (ex. 800x600, 1024x768) otherwise the loading screen is stretched to fit the screen,
which causes certain quality loss. Try to avoid gradients, because the client reduces the amount of colors used inside
the image as well.

## See Also
- [Login Background](./login-background.md)

[Category:Client Configuration](Category:Client_Configuration "wikilink")
