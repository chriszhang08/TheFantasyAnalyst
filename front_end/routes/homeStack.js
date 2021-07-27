import { createStackNavigator } from "react-navigation-stack";
import { createAppContainer } from "react-navigation";
import Home from "../app/screens/WelcomeScreen.js";
import ScheduleScreen from "../app/screens/ScheduleScreen.js";
import ImportWeekScreen from "../app/screens/ImportWeekScreen.js";
import AnalysisScreen from "../app/screens/AnalysisScreen.js";

const screens = {
  Home: {
    screen: Home,
  },
  AnalysisScreen: {
    screen: AnalysisScreen,
  },
  ScheduleScreen: {
    screen: ScheduleScreen,
  },
  ImportWeekScreen: {
    screen: ImportWeekScreen,
  },
};

const HomeStack = createStackNavigator(screens);

export default createAppContainer(HomeStack);
