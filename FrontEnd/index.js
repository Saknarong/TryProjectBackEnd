/**
 * @format
 */

import {AppRegistry} from 'react-native';
import App from './App';
import {name as appName} from './app.json';
import Test from './app/components/Test';
import ClothesDetail from './ClothesDetail';
import ShowDetailOfUser from './ShowDetailOfUser';
import SelectPageFemale from './SelectPageFemale';
import SelectPageMale from './SelectPageMale';


AppRegistry.registerComponent(appName, () =>SelectPageFemale);
