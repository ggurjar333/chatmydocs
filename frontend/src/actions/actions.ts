// actions.ts

// Define action types as string literals
export enum ActionType {
  INCREMENT = 'INCREMENT',
  DECREMENT = 'DECREMENT',
}

// Define action creators with TypeScript annotations
export const increment = (): { type: ActionType.INCREMENT } => {
  return {
    type: ActionType.INCREMENT,
  };
};

export const decrement = (): { type: ActionType.DECREMENT } => {
  return {
    type: ActionType.DECREMENT,
  };
};
