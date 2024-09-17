# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh


Program requirements:

1. When a user presses down one or more keys, those keys should appear "pressed" on the onscreen keyboard.
2. When a user lifts up one or more keys that were pressed, those keys should become "unpressed" on the onscreen keyboard.
3. When the user presses the shift key, the onscreen keyboard should display the "capitalized" version of each letter/number.
4. The page displays the next key that the user must press to render the next character in the typing tutor with a red shadow instead of the grey of the other keys
5. Once that key is pressed, the hint should move to the next key in the phrase. 
6. When the shift key is required, both shift keys should be highlighted
7. The page displays a keyboard where each key should look three dimensional as well as match key placements on a typical keyboard excluding certain keys like the delete key. 

8. The page displays a phrase for the user to type which should be replaced with another as soon as the user has finished typing it correctly. 
9. when the user types the phrase, the typed text should change to black
10. The page displays Untyped text in a light blue color
11. The next character to be typed should be the light blue of untyped text but underlined. 
12. the phrase on the screen is centered
13. When the user hits a wrong key, no changes occur in the phrase, but the keyboard still shows the keys being pressed. 
14. When the user reached a space character that need to be typed, the empty space will still be underlined unless the space is at the end of a line. 

15. Once the user has types all the phrases, the phrases are looped through again. 
