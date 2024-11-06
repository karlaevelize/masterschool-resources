import { useState } from "react";
import { ButtonPurple } from "./ButtonPurple";

export const Counter = () => {
  const [counter, setCounter] = useState(0);

  const increaseCounter = () => {
    setCounter(counter + 1);
  };

  const decreaseCounter = () => {
    setCounter(counter - 1);
  };

  return (
    <div>
      <h2>This is my Counter component</h2>
      <p>{counter > 0 ? "You have money" : "You are poor"}</p>
      <div onClick={increaseCounter}>
        <ButtonPurple text="+" />
      </div>
      <p>{counter}</p>
      <div onClick={decreaseCounter}>
        <ButtonPurple text="-" />
      </div>
    </div>
  );
};
