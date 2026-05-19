import { test, expect } from '@playwright/test';

test.describe('App smoke', () => {
  test('should open chat page', async ({ page }) => {
    await page.goto('/chat');

    await expect(page.getByText('LocalScript AI')).toBeVisible();
    await expect(page.getByText('Рабочая область')).toBeVisible();
    await expect(page.getByPlaceholder('Опиши задачу для Lua-агента...')).toBeVisible();
  });
});

test('should allow entering prompt text', async ({ page }) => {
  await page.goto('/chat');

  const textarea = page.getByPlaceholder(
    'Опиши задачу для Lua-агента...',
  );

  await textarea.fill('print("hello")');

  await expect(textarea).toHaveValue('print("hello")');
});

test('should create new run after prompt submission', async ({ page }) => {
  await page.goto('/chat');

  const textarea = page.getByPlaceholder(
    'Опиши задачу для Lua-агента...',
  );

  const runs = page.locator('.run-item__title');

  await expect(textarea).toBeVisible();

  await page.waitForLoadState('networkidle');

  const runsBefore = await runs.count();

  await textarea.fill('print("hello")');

  await page.getByRole('button', { name: 'Отправить' }).click();

  await expect
    .poll(async () => runs.count(), {
      timeout: 15000,
    })
    .toBeGreaterThan(runsBefore);
});

test('should show generation state after prompt submission', async ({ page }) => {
  await page.goto('/chat');

  const textarea = page.getByPlaceholder(
    'Опиши задачу для Lua-агента...',
  );

  await textarea.fill('print("hello")');

  await page.getByRole('button', { name: 'Отправить' }).click();

  await expect(
    page.getByText(/Генерируется|Проверяю модель/i),
  ).toBeVisible({
    timeout: 10000,
  });
});

