// store.ts

import { legacy_createStore } from 'redux';
import rootReducer from '../reducers/rootReducer'; // Import your rootReducer


const store = createStore(rootReducer);

export default store;

// Define your state interface
// export interface AppState {
//   counter: number;
// }
//
// // Define action types and creators
// export enum ActionType {
//   INCREMENT = 'INCREMENT',
//   DECREMENT = 'DECREMENT',
// }
//
// interface IncrementAction {
//   type: ActionType.INCREMENT;
// }
//
// interface DecrementAction {
//   type: ActionType.DECREMENT;
// }
//
// type Action = IncrementAction | DecrementAction;
//
// // Define the reducer
// const initialState: AppState = {
//   counter: 0,
// };
//
// const rootReducer = (state: AppState = initialState, action: Action): AppState => {
//   switch (action.type) {
//     case ActionType.INCREMENT:
//       return { ...state, counter: state.counter + 1 };
//     case ActionType.DECREMENT:
//       return { ...state, counter: state.counter - 1 };
//     default:
//       return state;
//   }
// };
//
// // Create the store
// const store = legacy_createStore(rootReducer);
//
// export default store;
