<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import type { Ref } from 'vue'

// CONSTANTS
const API_URL = 'http://127.0.0.1:8000/num_to_english'

// DATA
const num = defineModel({default: 12345678})
const chosenNumber: Ref<number | null> = ref(null)
const numInEnglish: Ref<number | null> = ref(null)


const loadingPOST = ref(false)
const warning = ref("");
const error = ref("");


// WATCH
watch(num, (newNum, oldNum) => {
  error.value = "" // remove error message if number changes
  
  if (newNum < 0) {
    warning.value = `${newNum} is less than 0.`
  } else if (newNum > 1000000000) {
    warning.value = `${newNum} is greater than 1,000,000,000.`
  } else {
    warning.value = ""
  }
})

// COMPUTED
const disableButtons = computed(() => {
  return loadingPOST.value || warning.value !== ""
});


// METHODS
async function getNumberAsEnglish(n: number) {
  const response = await fetch(API_URL + `?num=${n}`)
  chosenNumber.value = n

  const result = await response.json()

  if (result.status === "ok") {
    numInEnglish.value = result.num_in_english
  } else {
    error.value = result.status
  }

}

async function postNumberAsEnglish(n: number) {
  chosenNumber.value = n
  loadingPOST.value = true
  numInEnglish.value = null
  const response = await fetch(API_URL, {
    method: 'POST',
    body: JSON.stringify({
      number: n
    })
  })
  loadingPOST.value = false

  const result = await response.json()

  if (result.status === "ok") {
    numInEnglish.value = result.num_in_english
  } else {
    error.value = result.status
  }
}
</script>

<template>
  <main class="container" style="width: 500px;">
    <h1 class="text-center">Numbers to English</h1>
    <p class="text-center">Convert any number from 0 to 1,000,000,000 to English!</p>

    <div v-if="warning" class="alert alert-danger">
      <p class="m-0">{{ warning }}</p>
    </div>

    <div class="row">
      <label for="num" class="col fw-bold">Pick a number!</label>
      <input id="num" type="number" v-model="num" class="form-control col" min="0" max="1000000000" />
    </div>

    <div class="my-2 d-flex justify-content-between">
      <button @click="getNumberAsEnglish(num)" class="btn btn-primary" :disabled="disableButtons">GET</button>
      <button @click="postNumberAsEnglish(num)" class="btn btn-secondary" :disabled="disableButtons">POST</button>
    </div>
    
    <div v-if="error" class="alert alert-danger">
      <p>{{error}}</p>
    </div>
    
    <div v-if="chosenNumber !== null">
      <p class="text-center">You chose the number {{ chosenNumber }}. This number in English is...</p>

      <div v-if="loadingPOST" class="d-flex justify-content-center">
        <div class="spinner-grow" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
      
      <h6 class="text-center">
        {{ numInEnglish }}
      </h6>
    </div>

  </main>
</template>

<style scoped></style>
