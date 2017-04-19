import { combineReducers } from 'redux';
import Sample from './SampleReducers';

const rootReducer = combineReducers({
	sampleCheck: Sample
});

export default rootReducer;