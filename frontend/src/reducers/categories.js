import { GET_CATEGORY_LIST, DELETE_CATEGORY, ADD_CATEGORY, TOGGLE_CATEGORY } from "../actions/types";

const initialState = {
    categories: []
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_CATEGORY_LIST:
            return {
                ...state,
                categories: action.payload
            };
        case DELETE_CATEGORY:
            return {
                ...state,
                categories: state.categories.filter(ThirdCategory => ThirdCategory.id != action.payload)
                };
        case TOGGLE_CATEGORY:
            return {
                ...state,
                categories: [...state.categories]
                };
        case ADD_CATEGORY:
            return {
                ...state,
                categories: [...state.categories, action.payload]
                };
        default:
                return state;
    }
};
