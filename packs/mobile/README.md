# Pack: Mobile Applications

Use for native or cross-platform mobile projects.

## Standards
- Detect framework, supported OS versions, navigation, state management, permissions, and release process.
- Test small and large screens, keyboard behavior, safe areas, loading, offline, and error states.
- Request permissions only when needed and explain the user value.
- Handle deep links and authentication lifecycle safely.
- Avoid storing secrets in the app bundle.
- Check accessibility, reduced motion, and platform conventions.

## Suggested tools
- Expo: https://github.com/expo/expo (React Native projects)
- Maestro: https://github.com/mobile-dev-inc/maestro
- Platform-specific official documentation

## Verification
Run unit/integration tests and device/simulator journeys for critical flows. Clearly distinguish simulator coverage from physical-device testing.
