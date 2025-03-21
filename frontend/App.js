import React, { useState } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import Header from './components/Header';
import UploadForm from './components/UploadForm';
import Summary from './components/Summary';

export default function App() {
  const [summary, setSummary] = useState(null);

  const handleUpload = async (file) => {
    // TODO: Envoyer le fichier au backend
    console.log('Fichier téléchargé:', file);
    setSummary("Résumé généré par l'IA");
  };

  return (
    <View style={styles.container}>
      <Header />
      <UploadForm onUpload={handleUpload} />
      {summary && <Summary content={summary} />}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
});
