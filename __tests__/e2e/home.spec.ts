import { expect, test } from '@playwright/test'

test('has title', async ({ page }) => {
  await page.goto('/')

  await expect(page).toHaveTitle(/Anki Converter/)
})

test('upload file', async ({ page }) => {
  await page.goto('/')

  const filePath = './public/IBSYS I Anki Cards.md'
  await page.setInputFiles('input[name="file"]', filePath)

  await page.getByRole('button', { name: 'Upload' }).click()
})
