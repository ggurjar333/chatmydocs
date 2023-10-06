// Counter.tsx

import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement } from '../actions'; // Import actions
import { AppState } from '../store'; // Import your AppState type

const Counter: React.FC = () => {
  const counter = useSelector((state: AppState) => state.counter);
  const dispatch = useDispatch();

  return (
    <div>
      <h1>Counter: {counter}</h1>
      <button onClick={() => dispatch(increment())}>Increment</button>
      <button onClick={() => dispatch(decrement())}>Decrement</button>
    </div>
  );
};

export default Counter;
