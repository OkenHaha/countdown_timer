import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: 'http://127.0.0.1:8000',

  }
})

/*,
  server: {
    proxy:{
      "/api": "http://localhost:8000/timerapi/"
    }
  }*/
