// counterReducer.ts
import { ActionType } from "../actions/actions";

interface CounterState {
  counter: number;
}

const initialState = {
  counter: 0,
};

type ActionTypes = ActionType.INCREMENT | ActionType.DECREMENT;

const counterReducer = (state: CounterState = initialState, action: { type: ActionTypes }): CounterState => {
  switch (action.type) {
    case ActionType.INCREMENT:
      return { ...state, counter: state.counter + 1 };
    case ActionType.DECREMENT:
      return { ...state, counter: state.counter - 1 };
    default:
      return state;
  }
};

export default counterReducer;
