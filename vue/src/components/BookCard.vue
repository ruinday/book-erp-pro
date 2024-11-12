<script setup lang='ts'>
import { useSwitchStore } from '@/stores/show';
import { ref } from 'vue';
import { add_data } from '@/request/api';

const book = ref('')
const author = ref('')
const price = ref()
const publish_date = ref()
const publisher = ref('')

async function add_book() {
  await add_data({
    'name': book.value,
    'author': author.value,
    'price': price.value,
    'publish_date': publish_date.value,
    'publisher': publisher.value
  })
  useSwitchStore().show_change()
  location.reload()
}

</script>

<template>
  <div class="bc-container" v-show="useSwitchStore().show_add">
    <p class="close" @click="useSwitchStore().show_change">X</p>
    <p class="title">新增图书</p>
    <input v-model="book" type="text" placeholder="书名" autofocus required>
    <input v-model="author" type="text" placeholder="作者" required>
    <input v-model="price" type="number" placeholder="价格">
    <input v-model="publish_date" type="date" placeholder="出版时间" required>
    <input v-model="publisher" type="text" placeholder="出版社">
    <button @click="add_book()">新增</button>
  </div>
</template>

<style lang='scss' scoped>
@import '/src/assets/main.scss';

.bc-container {
  width: 400px;
  margin-top: -10vh;
  border-radius: 6px;
  background: #fff;
  padding: 20px;
  box-shadow: 0 0 5px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;

  p.close {
    position: absolute;
    top: 0px;
    right: 20px;
    cursor: pointer;
  }

  p.title {
    font-size: 20px;
    font-weight: 500;
  }

  input {
    width: 100%;
    height: 30px;
    margin: 10px 0;
    border: $border;
    border-radius: 4px;

    &:focus {
      outline: none;
    }
  }

  button {
    width: 100%;
    height: 32px;
    border: 0;
    color: #fff;
    border-radius: 4px;
    background: $bgcolor;
    margin: 20px 0 40px 0;
  }

}
</style>
