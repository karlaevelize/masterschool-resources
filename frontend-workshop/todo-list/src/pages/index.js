import { ButtonPurple } from "@/components/ButtonPurple";
import { Counter } from "@/components/Counter";

export default function Home() {
  return (
    <>
      <h1>This is my first React App</h1>
      <ButtonPurple text="Button 1" />
      <ButtonPurple text="Button 2" />
      <ButtonPurple text="Button 3" />
      <Counter />
    </>
  );
}
