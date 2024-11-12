import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useSwitchStore = defineStore('switch', () => {
  const show_add = ref(false)
  const show_change = () => (show_add.value = !show_add.value)

  const show_mdf = ref(false)
  const show_mdf_change = () => (show_mdf.value = !show_mdf.value)

  return { show_add, show_change, show_mdf, show_mdf_change }
})
