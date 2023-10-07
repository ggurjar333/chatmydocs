// store.ts

import { createStore } from 'redux';
import rootReducer from '../reducers/rootReducer'; // Import your rootReducer


const store = createStore(rootReducer);

export default store;

// Define your state interface
export interface AppState {
  counter: number;
}