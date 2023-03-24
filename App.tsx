import { StatusBar } from 'expo-status-bar';
import React, { useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { useFonts } from 'expo-font';
import { createStackNavigator } from "@react-navigation/stack";
import { NavigationContainer } from '@react-navigation/native';
import { Color } from './GlobalStyles';

import OnboardingScreen from './screens/OnboardingScreen';
import LoginScreen from './screens/LoginScreen';
import HomeScreen from './screens/HomeScreen';
// import Icon from 'react-native-vector-icons/Ionicons';


const AppStack = createStackNavigator();


export default function App() {
  const [hideSplashScreen, setHideSplashScreen] = React.useState(false);

  const [fontsLoaded, error] = useFonts({
    'Inter-Bold': require("./assets/fonts/Inter-Bold.ttf"),
    'Inter-Thin': require("./assets/fonts/Inter-Thin.ttf"),
    'Inter-Light': require("./assets/fonts/Inter-Light.ttf"),
    'Inter-Regular': require("./assets/fonts/Inter-Regular.ttf"),
    'Inter-SemiBold': require("./assets/fonts/Inter-SemiBold.ttf")
  });
  React.useEffect(() => {
    setTimeout(() => {
      setHideSplashScreen(true);
    }, 1000);
  }, []);

  if (!fontsLoaded && !error) {
    return null;
  }

  return (
    <NavigationContainer>
       <AppStack.Navigator
        screenOptions={{
          headerShown: false
        }}
       >
        <AppStack.Screen name="Onboarding" component={OnboardingScreen}/>
        <AppStack.Screen name="Login" component={LoginScreen}/>
        <AppStack.Screen name="Home" component={HomeScreen}/>

       </AppStack.Navigator>
    </NavigationContainer>
  );
}


