import { StatusBar } from "expo-status-bar";
import * as React from "react";
import { StyleSheet, Text, View } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { useFonts } from "expo-font";

import { createStackNavigator } from "@react-navigation/stack";
import { NavigationContainer } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { Color } from "./GlobalStyles";
import OnboardingScreen from "./screens/OnboardingScreen";
import LoginScreen from "./screens/LoginScreen";
import RegisterScreen from "./screens/RegisterScreen";
import HomeScreen from "./screens/HomeScreen";
import DetailsScreen from "./screens/DetailsScreen";
import SettingsScreen from "./screens/SettingsScreen";
import DetailScreen from "./screens/DetailsScreen";
import LedScreen from "./screens/LedScreen";
import FanScreen from "./screens/FanScreen";
import LedSettingScreen from "./screens/LedSettingScreen";
import FanSettingScreen from "./screens/FanSettingScreen";

// import Icon from 'react-native-vector-icons/Ionicons';

const Stack = createStackNavigator();

const Tab = createBottomTabNavigator();

const checkFirstLaunch = async () => {
  const isFirstLaunch = await AsyncStorage.getItem("alreadyLaunched");
  if (isFirstLaunch == null) {
    AsyncStorage.setItem("alreadyLaunched", "true");
    return true;
  }
  return false;
};

export default function App() {
  const [hideSplashScreen, setHideSplashScreen] = React.useState(false);
  const [isFirstLaunch, setIsFirstLaunch] = React.useState(null);

  const [fontsLoaded, error] = useFonts({
    "Inter-Bold": require("./assets/fonts/Inter-Bold.ttf"),
    "Inter-Thin": require("./assets/fonts/Inter-Thin.ttf"),
    "Inter-Light": require("./assets/fonts/Inter-Light.ttf"),
    "Inter-Regular": require("./assets/fonts/Inter-Regular.ttf"),
    "Inter-SemiBold": require("./assets/fonts/Inter-SemiBold.ttf"),
  });
  // React.useEffect(() => {
  //   setTimeout(() => {
  //     setHideSplashScreen(true);
  //   }, 1000);
  // }, []);

  React.useEffect(() => {
    checkFirstLaunch().then((result) => setIsFirstLaunch(result));
  }, []);

  if (!fontsLoaded && !error) {
    return null;
  }

  if (isFirstLaunch === null) {
    return null;
  } else if (isFirstLaunch === true) {
    return (
      <NavigationContainer>
        <Stack.Navigator
          screenOptions={{
            headerShown: false,
          }}
        >
          <Stack.Screen name="Onboarding" component={OnboardingScreen} />
          <Stack.Screen name="LoginScreen" component={LoginScreen} />
          <Stack.Screen name="RegisterScreen" component={RegisterScreen} />
          <Stack.Screen name="HomeScreen" component={HomeScreen} />
          <Stack.Screen name="DetailsScreen" component={DetailsScreen} />
          <Stack.Screen name="SettingsScreen" component={SettingsScreen} />
          <Stack.Screen name="LedScreen" component={LedScreen} />
          <Stack.Screen name="FanScreen" component={FanScreen} />
          <Stack.Screen name="LedSettingScreen" component={LedSettingScreen} />
          <Stack.Screen name="FanSettingScreen" component={FanSettingScreen} />
        </Stack.Navigator>
      </NavigationContainer>
    );
  } else {
    return (
      <NavigationContainer>
        <Stack.Navigator
          screenOptions={{
            headerShown: false,
          }}
        >
          <Stack.Screen name="LoginScreen" component={LoginScreen} />
          <Stack.Screen name="RegisterScreen" component={RegisterScreen} />
          <Stack.Screen name="HomeScreen" component={HomeScreen} />
          <Stack.Screen name="DetailsScreen" component={DetailsScreen} />
          <Stack.Screen name="SettingsScreen" component={SettingsScreen} />
          <Stack.Screen name="LedScreen" component={LedScreen} />
          <Stack.Screen name="FanScreen" component={FanScreen} />
          <Stack.Screen name="LedSettingScreen" component={LedSettingScreen} />
          <Stack.Screen name="FanSettingScreen" component={FanSettingScreen} />
        </Stack.Navigator>
      </NavigationContainer>
    );
  }
}
