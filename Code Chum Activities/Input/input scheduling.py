postDate = input('Enter Post Date: ')
postTime = input('Enter Post Time: ')
postReach = float(input('Enter Post Reach: '))
postEngagement = float(input('Enter Post Engagement: '))
postDuration = float(input('Enter Post Duration: '))
postCategory = input('Enter Post Category: ')

reachDoubleFloat = f"{postReach:.2f}"
durationDoubleFloat = f"{postDuration:.2f}"
engagementDoubleFloat = f"{postEngagement:.2f}"

print()
print('Post Scheduled:')
print('Date:',postDate,'\nTime:',postTime,'\nReach:',reachDoubleFloat)
print('Engagement:',engagementDoubleFloat,'\nDuration:',durationDoubleFloat,'\nCategory:',postCategory)