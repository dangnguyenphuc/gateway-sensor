import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

export default function LoginScreen({navigation}: {navigation: any}) {
    return (
        <View style={styles.container}>
            <Text> Login Screen </Text>
            <Button 
                title="Click Here"
                onPress={() => navigation.navigate("Home")}
            />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center'
    },
});