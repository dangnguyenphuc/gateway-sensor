import React from "react";
import { View, Text, Button, StyleSheet } from "react-native";

export default function LoginScreen({ navigation }: { navigation: any }) {
  return (
    <View style={styles.container}>
      <Text> Login Screen </Text>
      <Button
        title="This is Login Screen"
        onPress={() => navigation.navigate("HomeScreen")}
      />
      <Text>LED Screen</Text>
      <Button
        title="This is Led Screen"
        onPress={() => navigation.navigate("LedScreen")}
      />
      <Text>Fan Screen</Text>
      <Button
        title="This is Fan Screen"
        onPress={() => navigation.navigate("FanScreen")}
      />
      <Text>Led Setting Screen</Text>
      <Button
        title="This is Led Setting Screen"
        onPress={() => navigation.navigate("LedSettingScreen")}
      />
      <Text>Led Setting Screen</Text>
      <Button
        title="This is Fan Setting Screen"
        onPress={() => navigation.navigate("FanSettingScreen")}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
});
