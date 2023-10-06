// rootReducer.ts

import { combineReducers } from 'redux';
import counterReducer from './counterReducer'; // Import your individual reducers

const rootReducer = combineReducers({
  counter: counterReducer,
  // Add other reducers here if needed
});

export default rootReducer;
