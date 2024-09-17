import './App.css'

import { TypingTutor } from './TypingTutor'
import { Keyboard } from './Keyboard';
import { useEffect, useState } from 'react'

const phrases = [
  "Many fairy tales begin with a \"once upon a time\".", 
  "A lonely mermaid discovered magic pearls in the depths of the ocean.",
  "A small, forgotten garden bloomed with flowers that whispered secrets to those who listened closely.",
  "The old, dusty mirror in the attic revealed the future, but its visions came at a price.",
  "A kind, talking fox helped a lost child find their way home through the enchanted forest.",
  "A crafty, hardworking spider wove webs that told stories to the moon.",
  "A mischievous pixie left tiny, glowing footprints wherever it danced.",
  "A magical feather granted its possessor the ability to soar through the skies with the birds.",
  "In a tiny cottage, a cobbler's shoes had the power to grant a wish to anyone who wore them.",
   "The fierce dragon guarded a treasure chest of dreams, waiting for a brave hero to set them free."
];
const shiftList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", "\"", "<", ">", "?"];

function App() {

  const [phraseIndex, setPhraseIndex] = useState(0);
  const [nextPhrase, setNextPhrase] = useState(phrases[phraseIndex]);
  const [charIndex, setCharIndex] = useState(0);
  const[typed, setTyped] = useState("");
  const[nextChar, setNextChar] = useState(phrases[0][0]);
  const[untyped, setUntyped] = useState(phrases[0].substring(1));
  const[keys, setKeys] = useState([]);
  const[shift, setShift] = useState(false);

  function isUpperCase(char) {
    return char === char.toUpperCase() && char !== char.toLowerCase();
  }


  useEffect(() => {
    if(isUpperCase(nextChar) || shiftList.includes(nextChar)){
      setShift(true);
    }
    function keydown(e){
      if (e.repeat) return; // keydown event trigger rapidly if you hold the key, we only want to detect keydown once.
        //check to see which key they typed
        setKeys([...keys, e.key]);

        //when user types correct char, add char to the typed and remove from untyped move to next char
        if(e.key == nextChar){
          //add char to typed characters
          setTyped(typed + e.key);
          //increment charIndex
          setCharIndex((prevIndex) => (prevIndex + 1));
          //remove char from untyped
          setUntyped(untyped.substring(1));
          //set the next char
          setNextChar(phrases[phraseIndex][charIndex + 1]);

          //if user reaches the end of the phrase, replace it with a new phrase
          if(charIndex + 1 === nextPhrase.length){
            //get the next phrase
            setPhraseIndex((prevIndex) => (prevIndex + 1) % phrases.length);
            setNextPhrase(phrases[(phraseIndex + 1) % phrases.length]); 
            //remove the old phrase
            setCharIndex(0);
            setTyped("");
            //replace it with a new one
            setUntyped(phrases[(phraseIndex + 1) % phrases.length].substring(1));
            setNextChar(phrases[(phraseIndex + 1) % phrases.length][0]);
            //reset shift state
            setShift(false);
          }
        }
    }
    window.addEventListener("keydown", keydown);
    function keyup(e){
      // remove the keys from the list of pressed keys on keyup event
      const newKeys = [...keys];
      newKeys.splice(newKeys.indexOf(e.key), 1);
      setKeys(newKeys);

      // Reset the shift state when the Shift key is released
      if (e.key === "Shift") {
        setShift(false);
      }

    }
    window.addEventListener("keyup", keyup);

    //clean up
    return () => {
        window.removeEventListener("keydown", keydown);
        window.removeEventListener("keyup", keyup);
      };
  });

  return (
      <main className='content'>
        <TypingTutor typed={typed} nextChar={nextChar} untyped={untyped}/>
        <Keyboard keys={keys} nextChar={nextChar} isShift={shift}/>
      </main>
  );
}

export default App
